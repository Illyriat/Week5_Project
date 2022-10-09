from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.mic import Mic
from repositories.mic_repository as mic_repository