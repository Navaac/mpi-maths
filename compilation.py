#!/usr/bin/env python3

import argparse
import subprocess
import re
from pathlib import Path

CHAPTERS_LOCATION = "./"

BUILD_DIR = CHAPTERS_LOCATION + "build/"
C_CHAPITRES_DIR = BUILD_DIR + "chapitres/"
C_COURS_DIR = BUILD_DIR + "cours/"
C_TD_DIR = BUILD_DIR + "TDs/"
C_INTEGRALE_DIR = BUILD_DIR + "integrale/"

LATEX_COMPILER = "pdflatex"
GARBAGE_EXTENSIONS = {
    ".aux", ".log", ".toc", ".out", ".synctex.gz", 
    ".fls", ".fdb_latexmk", ".lof", ".lot", ".bcf", ".run.xml"
}

parser = argparse.ArgumentParser(description="Compilation script for MPI math course.")

parser.add_argument("-ch", "--chapitres", default="all", help="Chapters to compile, default : all.")
parser.add_argument("-m", "--mode", default="chapitre", help="What to compile, default : chapitre, options : chapitre, cours, TD." )

args = parser.parse_args()

chapters_path = Path(CHAPTERS_LOCATION).resolve()

target_dirs = [
    d for d in chapters_path.iterdir() 
    if d.is_dir() and d.name.startswith("chapitre") and d.name != "chapitre0"
]

if args.chapitres.lower() != "all" and args.chapitres.lower() != "integrale" :
    target_numbers = {num.strip() for num in args.chapitres.split(",")}
    target_dirs = [d for d in target_dirs if (m := re.search(r"(\d+)$", d.name)) and m.group(1) in target_numbers]

build_dir = Path(BUILD_DIR).resolve()
build_dir.mkdir(exist_ok=True)

def clean_dir (dir) :
    for file in dir.iterdir():
        if file.is_file() and file.suffix in GARBAGE_EXTENSIONS :
            file.unlink()
    return

def compile_file (file, output_dir, cwd_path) :
    cwd_dir = Path(cwd_path).resolve()
    
    result = subprocess.run(
                            [
                                LATEX_COMPILER,
                                f"-output-directory={output_dir}",
                                "-interaction=nonstopmode",
                                "-halt-on-error",
                                file
                            ],
                            capture_output=True,
                            cwd=cwd_dir
                        )

    if(result.returncode != 0) :
        print("ERROR : Compilation failed for ", file)
        exit(1)
    return

def compile_chapters (targets, dir) :
    for chapitre in targets :
        chapter_number = int(chapitre.name.replace("chapitre", ""))
        compile_file(str(chapitre) + "/chapitre" + str(chapter_number) + ".tex", str(dir), str(chapitre))

    return

def compile_cours (targets, dir) :
    for chapitre in targets :
        chapter_number = int(chapitre.name.replace("chapitre", ""))
        compile_file(str(chapitre) + "/cours/" + "cours" + str(chapter_number) + ".tex", str(dir), str(chapitre) + "/cours/")
        
    return  

def compile_TDs (targets, dir) :
    for chapitre in targets :
        chapter_number = int(chapitre.name.replace("chapitre", ""))
        compile_file(str(chapitre) + "/TD/" + "TD" + str(chapter_number) + ".tex", str(dir), str(chapitre) + "/TD/")

    return

if args.chapitres == "integrale" :
    c_integrale_dir = Path(C_INTEGRALE_DIR).resolve()
    c_integrale_dir.mkdir(exist_ok=True)

    match args.mode :
        case "chapitre" :
            compile_file(str(chapters_path) + "/integrale/integrale_mpi.tex", str(c_integrale_dir), str(chapters_path) + "/integrale/")
            compile_file(str(chapters_path) + "/integrale/integrale_mpi.tex", str(c_integrale_dir), str(chapters_path) + "/integrale/")
        case "cours" :
            compile_file(str(chapters_path) + "/integrale/integrale_cours.tex", str(c_integrale_dir), str(chapters_path) + "/integrale/")
            compile_file(str(chapters_path) + "/integrale/integrale_cours.tex", str(c_integrale_dir), str(chapters_path) + "/integrale/")
        case "TD" :
            compile_file(str(chapters_path) + "/integrale/integrale_TD.tex", str(c_integrale_dir), str(chapters_path) + "/integrale/")
            compile_file(str(chapters_path) + "/integrale/integrale_TD.tex", str(c_integrale_dir), str(chapters_path) + "/integrale/")
        case _ :
            print("ERROR: invalid input for mode field.")
            exit(1)

    clean_dir(c_integrale_dir)
else :
    match args.mode :
        case "chapitre" :
            c_chapters_dir = Path(C_CHAPITRES_DIR).resolve()
            c_chapters_dir.mkdir(exist_ok=True)
        
            compile_chapters(target_dirs, c_chapters_dir)
            compile_chapters(target_dirs, c_chapters_dir)
        
            clean_dir(c_chapters_dir)
        case "cours" :
            c_cours_dir = Path(C_COURS_DIR).resolve()
            c_cours_dir.mkdir(exist_ok=True)
        
            compile_cours(target_dirs, c_cours_dir)
            compile_cours(target_dirs, c_cours_dir)

            clean_dir(c_cours_dir)
        case "TD" :
            c_TDs_dir = Path(C_TD_DIR).resolve()
            c_TDs_dir.mkdir(exist_ok=True)
        
            compile_TDs(target_dirs, c_TDs_dir)
            compile_TDs(target_dirs, c_TDs_dir)

            clean_dir(c_TDs_dir)
        case _ :
            print("ERROR: invalid input for mode field.")
            exit(1)
        
print("Compilation finished, pdf are in the build subdir.")
