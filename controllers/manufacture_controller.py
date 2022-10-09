from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacture import Manufacture
from repositories.manufacture_repository as manufacture_repository