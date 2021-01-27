#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {'1а': 25, '1б': 24, '2б': 27, '6а': 23, '7а': 25, '7в': 31, '11а': 29, '11б': 28}
    print(school)
    school['1а'] = 30
    school['10в'] = 25
    del school['7в']
    total = 0
    for group in school:
        total += school[group]
    print(school)
    print(total)


