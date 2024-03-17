from browser import document, html, window, alert
import random 
def sketch(p):#processes the sketch itself p is needed.to do background color 
  #background(0) instead of p.background(0)
  def setup():
    p.createCanvas(2000,800)#size of the canvas
    p.background(255)#background color
    p.rectMode(p.CENTER)
  def draw():
    colorlist = ['purple', 'orange', 'red', 'blue', 'yellow']
    p.noStroke()
    p.fill(random.choice(colorlist))
    p.ellipse(p.mouseX, p.mouseY, 50,50)
  def mousePressed(self):
    p.background(0)
  def keyPressed(self):
    if p.key == " ": 
      print("ALOHA!!")
  p.setup = setup 
  p.draw = draw
  p.mousePressed = mousePressed
  p.keyPressed = keyPressed
myp5 = window.p5.new(sketch)