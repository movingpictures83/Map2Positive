import sys
#import numpy
import random


class Map2PositivePlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line)

      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      for i in range(self.n):
         if self.bacteria[i][0] == '\"':
            self.bacteria[i] = self.bacteria[i][1:len(self.bacteria[i])-1]
         self.bacteria[i] = self.bacteria[i].strip()
      self.ADJ = []#numpy.zeros([self.m, self.n])
      i = 0
      for i in range(self.m):
            self.ADJ.append([])
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               #print contents[j+1]
               value = float(contents[j+1])
               #print self.ADJ[i][j]
               self.ADJ[i].append(value)#[j] = value
            i += 1
  
   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      filestuff2.write("name\tmappedWeight\n")
      #for i in range(self.m):
      #   sum = float(0.0)
      #   for j in range(self.n):
      #      sum += self.ADJ[i][j]
         #print "SUM: ", sum
      #   for j in range(self.n):
      #      self.ADJ[i][j] /= sum
            
      for i in range(self.m):
         #filestuff2.write(self.bacteria[i]+',')
         #filestuff2.write(self.samples[i]+',')
         for j in range(self.n):
            filestuff2.write(self.bacteria[i]+' '+'('+'interacts with'+')'+' '+self.bacteria[j]+'\t'+str(self.ADJ[i][j]+1)+'\n')
            #filestuff2.write(str(self.ADJ[i][j]+1))
            #if (j < self.n-1):
            #   filestuff2.write(",")
            #else:
            #   filestuff2.write("\n")



