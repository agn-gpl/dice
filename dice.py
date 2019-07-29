#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Copyright (C) 2019  AGN

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import random as rd

def dice(n,s,z=False):
    out=""
    if z:
        for i in range(n):
            out+=f"{rd.randint(1,s)}, "
        out=out.rstrip(", ")+"\n"
    else:
        for i in range(n):
            out+=f"{rd.randint(1,s)}\n"
    return out

def choose(m,n,z=False):
    if n>m:
        return "ERROR: choose too many numbers\n"
    idx,out=rd.sample((range(1,m+1)),n),""
    if z:
        for i in range(n):
            out+=f'{idx[i]}, '
        out=out.rstrip(", ")+"\n"
    else:
        for i in range(n):
            out+=f'{idx[i]}\n'
    return out

def get_sum(n,s,r=1,z=False):
    out=""
    for i in range(r):
        temp=0
        for j in range(n):
            temp+=rd.randint(1,s)
        if z:
            out+=f"{temp}, "
        else:
            out+=f"{temp}\n"
    if z:
        out=out.rstrip(", ")+"\n"
    return out

def print_help():
    print('XdY: throw X Y-side dice(s).\nYcX: choose X number(s) from 1 to Y.\nXsY: get the sum of X Y-side dice(s).\nXsYxZ: get the sum of X Y-side dice(s) for Z times.\nadd "z" in front or back of the command to print the outcome in one line.\ninput "q" or "quit" to exit.')

def main():
    while True:
        npt,z=input("> ").strip(),False
        if npt=='':
            continue
        if npt.startswith("z") or npt.endswith("z"):
            z=True
        if npt.count("d")==1:
            tok=npt.lstrip("z").rstrip("z").split("d")
            print(dice(int(tok[0]),int(tok[1]),z),end="")
        elif npt.count("c")==1:
            tok=npt.lstrip("z").rstrip("z").split("c")
            print(choose(int(tok[0]),int(tok[1]),z),end="")
        elif npt.count("s")==1:
            tok=npt.lstrip("z").rstrip("z").split("s")
            print(get_sum(int(tok[0]),int(tok[1]),z),end="")
        elif npt.count("s")==2:
            tok=npt.lstrip("z").rstrip("z").split("s")
            print(get_sum(int(tok[0]),int(tok[1]),int(tok[2]),z),end="")
        elif npt=="h" or npt=="help":
            print_help()
        elif npt=="q" or npt=="quit":
            break
        else:
            print(f'ERROR: Unknown command "{npt}"')
            
if __name__ == '__main__':
    main()
