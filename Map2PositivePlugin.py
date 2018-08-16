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
         self.bacteria[i] = self.bacteria[i].strip()
         if self.bacteria[i][0] == '\"':
            self.bacteria[i] = self.bacteria[i][1:len(self.bacteria[i])-1]
      self.ADJ = []
      i = 0
      for i in range(self.m):
            self.ADJ.append([])
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               value = float(contents[j+1])
               self.ADJ[i].append(value)
            i += 1
  
   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      filestuff2.write("name\tmappedWeight\n")
            
      for i in range(self.m):
         for j in range(self.n):
            if (self.ADJ[i][j] <= 0):
               filestuff2.write(self.bacteria[i]+' '+'('+'pp'+')'+' '+self.bacteria[j]+'\t'+str(0)+'\n')
            else:
               filestuff2.write(self.bacteria[i]+' '+'('+'pp'+')'+' '+self.bacteria[j]+'\t'+str(self.ADJ[i][j])+'\n')
            #filestuff2.write(self.bacteria[i]+' '+'('+'pp'+')'+' '+self.bacteria[j]+'\t'+str(self.ADJ[i][j]+1)+'\n')



