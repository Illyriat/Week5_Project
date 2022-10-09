from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.djequip import Djequip
from repositories.djequip_repository as djequip_repository
