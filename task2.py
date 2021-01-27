#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {25: '7а', 24: '1б', 27: '2б', 23: '6а', 31: '7в', 29: '11а', 28: '11б'}
    print(school)
    school_reverse = {}
    for key, value in school.items():
        school_reverse[value] = key
    print(school_reverse)
