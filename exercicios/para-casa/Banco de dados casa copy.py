{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3fb51551",
   "metadata": {},
   "source": [
    "## Banco de dados"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6f065d6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a7aa9973",
   "metadata": {},
   "outputs": [],
   "source": [
    "file = open(\"estilo_vida.csv\", encoding= 'latin-1'\n",
    " ) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "eaaee9c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "conteudo = csv.reader(file)\n",
    "\n",
    "connection = sqlite3.connect(\"Banco_estilo_vida.db\")\n",
    "\n",
    "cursor = connection.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "25d07ce5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x2773f78eac0>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "cursor.execute('''CREATE TABLE IF NOT EXISTS estilo_vida (\n",
    "    Person ID INT,\n",
    "    Gender VARCHAR,\n",
    "    Age VARCHAR, \n",
    "    Occupation FLOAT,\n",
    "    Sleep Duration VARCHAR,\n",
    "    Quality of Sleep FLOAR,\n",
    "    Physical Activity Level FLOAT,\n",
    "    Stress Level FLOAT,\n",
    "    BMI Category VARCHAR,\n",
    "    Blood Pressure VARCHAR,\n",
    "    Heart Rate VARCHAR, \n",
    "    Daily Steps VARCHAR,\n",
    "    Disorder VARCHAR\n",
    "    \n",
    ")''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "8a047292",
   "metadata": {},
   "outputs": [
    {
     "ename": "ProgrammingError",
     "evalue": "Cannot operate on a closed database.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mProgrammingError\u001b[0m                          Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\marci\\estudos\\semana13\\on26-python-s13-projeto-guiado-II\\exercicios\\para-casa\\Banco de dados casa.ipynb Cell 6\u001b[0m line \u001b[0;36m3\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/marci/estudos/semana13/on26-python-s13-projeto-guiado-II/exercicios/para-casa/Banco%20de%20dados%20casa.ipynb#W5sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m inserir_conteudo \u001b[39m=\u001b[39m \u001b[39m\"\u001b[39m\u001b[39mINSERT INTO estilo_vida  (Person ID,\tGender,\tAge\tOccupation,\tSleep Duration,\tQuality of Sleep, Physical Activity Level,\tStress Level,\tBMI Category,\tBlood Pressure,\tHeart Rate,\tDaily Steps, Disorder)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)\u001b[39m\u001b[39m\"\u001b[39m\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/marci/estudos/semana13/on26-python-s13-projeto-guiado-II/exercicios/para-casa/Banco%20de%20dados%20casa.ipynb#W5sZmlsZQ%3D%3D?line=2'>3</a>\u001b[0m cursor\u001b[39m.\u001b[39;49mexecute(inserir_conteudo, conteudo)\n",
      "\u001b[1;31mProgrammingError\u001b[0m: Cannot operate on a closed database."
     ]
    }
   ],
   "source": [
    "\n",
    "inserir_conteudo = \"INSERT INTO estilo_vida  (Person ID,\tGender,\tAge\tOccupation,\tSleep Duration,\tQuality of Sleep, Physical Activity Level,\tStress Level,\tBMI Category,\tBlood Pressure,\tHeart Rate,\tDaily Steps, Disorder)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)\"\n",
    "\n",
    "cursor.execute(inserir_conteudo, conteudo)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "51ed46b3",
   "metadata": {},
   "outputs": [
    {
     "ename": "OperationalError",
     "evalue": "no such table: estilo_vida",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOperationalError\u001b[0m                          Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\marci\\estudos\\semana13\\on26-python-s13-projeto-guiado-II\\exercicios\\para-casa\\Banco de dados casa.ipynb Cell 7\u001b[0m line \u001b[0;36m2\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/marci/estudos/semana13/on26-python-s13-projeto-guiado-II/exercicios/para-casa/Banco%20de%20dados%20casa.ipynb#W6sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m selecionar_tudo \u001b[39m=\u001b[39m \u001b[39m\"\u001b[39m\u001b[39mSELECT * FROM estilo_vida\u001b[39m\u001b[39m\"\u001b[39m\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/marci/estudos/semana13/on26-python-s13-projeto-guiado-II/exercicios/para-casa/Banco%20de%20dados%20casa.ipynb#W6sZmlsZQ%3D%3D?line=1'>2</a>\u001b[0m entradas \u001b[39m=\u001b[39m cursor\u001b[39m.\u001b[39;49mexecute(selecionar_tudo)\u001b[39m.\u001b[39mfetchall()\n",
      "\u001b[1;31mOperationalError\u001b[0m: no such table: estilo_vida"
     ]
    }
   ],
   "source": [
    "selecionar_tudo = \"SELECT * FROM estilo_vida\"\n",
    "entradas = cursor.execute(selecionar_tudo).fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f30ba732",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'entradas' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\marci\\estudos\\semana13\\on26-python-s13-projeto-guiado-II\\exercicios\\para-casa\\Banco de dados casa.ipynb Cell 8\u001b[0m line \u001b[0;36m1\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/marci/estudos/semana13/on26-python-s13-projeto-guiado-II/exercicios/para-casa/Banco%20de%20dados%20casa.ipynb#X10sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m \u001b[39mfor\u001b[39;00m entrada \u001b[39min\u001b[39;00m entradas:\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/marci/estudos/semana13/on26-python-s13-projeto-guiado-II/exercicios/para-casa/Banco%20de%20dados%20casa.ipynb#X10sZmlsZQ%3D%3D?line=1'>2</a>\u001b[0m   \u001b[39mprint\u001b[39m(entrada)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'entradas' is not defined"
     ]
    }
   ],
   "source": [
    "for entrada in entradas:\n",
    "  print(entrada)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a7dcca72",
   "metadata": {},
   "outputs": [],
   "source": [
    "connection.commit()\n",
    "connection.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "676a9111",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
