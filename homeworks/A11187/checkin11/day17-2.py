#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xiangrikui
import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('blue')
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')
	bran.speed(0.02)
	for i in range(1,40):
		turtle.position()
		(0.00,0.00)
		turtle.backward(30)
		turtle.position()
		(-30.00,0.00)
		
		turtle.heading()
		22.0
		turtle.left(45)
		turtle.heading()
		67.0


if __name__ == '__main__':
	main()
