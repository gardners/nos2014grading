#!/usr/bin/env python

import csv

count=0

with open('results.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=':', quotechar='|')
    for row in reader:
        if count>0:
            # Get raw exam marks
            raw_exam401 = int(row[4]);
            raw_exam402 = int(row[5]);
            # Scale them to reflect that they are 4-way multiple choice
            exam401 = (raw_exam401 - 25)*(100.0/75);
            if exam401<0: exam401=0
            exam402 = (raw_exam402 - 25)*(100.0/75);
            if exam402<0: exam402=0
            # Calculate average exam score
            examavg = ( exam401 + exam402 ) / 2

            # Get prac and tute marks
            pracs = int(row[2]);
            tutes = int(row[3]);
            # Calculate average prac and tute score
            pracavg = ( pracs + tutes ) / 2

            # Work out whether to replace pracs and tutes with exam results
            rule = 1;
            if (exam401 >= 80) and (exam402 >= 80):
                if examavg > pracavg:
                    pracavg = examavg
                    rule=2;

            # Get assignment result
            assignment = int(row[6]);
                    
            # work out total grade
            final = round( ( pracavg * 0.2 ) + ( examavg * 0.5 ) + ( assignment * 0.3 ) );

            if final < 45:
                grade = "F"
            elif final < 50:
                grade = "FA"
            elif final < 65:
                grade = "P"
            elif final < 75:
                grade = "CR"
            elif final < 85:
                grade = "DN"
            else:
                grade = "HD"
            
            print row[0] + ":" + row[1] + ":" + str(rule) + ":" + str(final) + ":" + grade
                
        count=count+1
