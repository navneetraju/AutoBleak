lex Convert.l
gcc lex.yy.c
./a.out < guess.txt > guess.json
python3 Tree.py > output.json
node getButtonQuerySelectors.js > queries.txt 
python3 autoscript.py
rm a.out lex.yy.c guess.json output.json queries.txt
