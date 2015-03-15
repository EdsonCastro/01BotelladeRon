{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Se genera una lista de 100 elementos, se invierte el orden con reverse y se elimina el 0, \n",
    "# con el objetivo de recorrer la lista y llegar \"0 bottles of beer on the wall.\n",
    "lista = range(100)\n",
    "lista.reverse()\n",
    "lista.pop()\n",
    "#print lista\n",
    "\n",
    "print \"                              Song Bottle of Beer.\\n\"\n",
    "for Elemento in lista :\n",
    "    print \"          \", Elemento, \"bottles of beer on the wall,\", Elemento, \"bottles of beer.\"\n",
    "    print \"          \", \"Take one down, pass it around,\", Elemento-1, \"bottles of beer on the wall.\"\n",
    "print \"\\n                              End of song\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
