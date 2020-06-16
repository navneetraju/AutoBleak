lex Convert.l
gcc lex.yy.c
./a.out < guess.txt > guess.json
python3 Tree.py > output.json
rm a.out lex.yy.c guess.json