#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 22:29:20 2020

@author: muhammadzahidi
"""
import time

print('-'*70)
print('                            Leap Year Finder')

def main():
    
    print('-'*70)
    
    time.sleep(2)
    
    userInput = int(input('Enter the year you would like to calculate:'))
    
    print('-'*70)
    
    print('Processing...')
    
    print('-'*70)
    
    time.sleep(3)
    
    if userInput % 4 != 0:
        
        print('The year {} is not a leap year'.format(userInput))
        
        print('-'*70)
        
    elif userInput % 4 == 0:
        
        if userInput % 100 != 0:
            
            print('The year {} is a leap year'.format(userInput))
            
            print('-'*70)
            
        elif userInput % 100 == 0:
            
            if userInput % 400 != 0:
                
                print('The year {} is not a leap year'.format(userInput))
                
                print('-'*70)
                
            elif userInput % 400 == 0:
                
                print('The year {} is a leap year'.format(userInput))
                
                print('-'*70)
                
                
                
while True:
    
    main()
    
    time.sleep(2)
    
    if str(input('Would you like to calculate again? (Y/N):')).upper().strip() != 'Y':
        
        print('\nGoodbye!\n')
        
        time.sleep(2)
        
        break
        
        
    
    