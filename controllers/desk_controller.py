from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.desk import Desk
from repositories.desk_repository as desk_repository