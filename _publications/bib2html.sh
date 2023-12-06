 
bibtex2html/bibtex2html -nf url_code "Code" -nf codec "C Code" -nf codecpp "C++ Code" -nf codemat "Matlab Code" -nf codejava "Java Code" -nf results Results publication-book.bib
bibtex2html/bibtex2html -nf url_code "Code" -nf codec "C Code" -nf codecpp "C++ Code" -nf codemat "Matlab Code" -nf codejava "Java Code" -nf results Results publication-journal.bib
bibtex2html/bibtex2html -nf url_code "Code" -nf codec "C Code" -nf codecpp "C++ Code" -nf codemat "Matlab Code" -nf codejava "Java Code" -nf results Results publication-conf.bib
bibtex2html/bibtex2html -nf url_code "Code" -nf codec "C Code" -nf codecpp "C++ Code" -nf codemat "Matlab Code" -nf codejava "Java Code" -nf results Results publication-chapter.bib
chmod go+r *.html



# add "TEVC Outstanding Paper Award" to the DG paper
sed -i '' 's+\[&nbsp;<a href="publication-journal_bib.html#omidvar2014cooperative"+ <b style="color:red;">(TEVC Outstanding Paper Award)</b> &nbsp;<a href="publication-journal_bib.html#omidvar2014cooperative"+g' publication-journal.html

# add "Best Paper Runner-Up Award" to Fang's AI2018 MTGP paper
sed -i '' 's+pages 472--484. Springer, 2018.+pages 472--484. Springer, 2018. <b style="color:red;">(Best Paper Runner-Up Award)</b>+g' publication-conf.html

# add "Best Paper Runner-Up" to Alex's ICWS2018 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#da2018hybrid"+ <b style="color:red;">(Best Paper Runner-Up)</b> &nbsp;<a href="publication-conf_bib.html#da2018hybrid"+g' publication-conf.html

# add "Best Paper Nomination" to Alex's EvoCOP2016 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#da2016particle"+ <b style="color:red;">(Best Paper Nomination)</b> &nbsp;<a href="publication-conf_bib.html#da2016particle"+g' publication-conf.html

# add "Best Paper" to Zhixing's EuroGP2022 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#huang2022investigation"+ <b style="color:red;">(Best Paper Award)</b> &nbsp;<a href="publication-conf_bib.html#huang2022investigation"+g' publication-conf.html

# add "Best Paper" to Shaolin's GECCO2022 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#wang2022local"+ <b style="color:red;">(ECOM Track Best Paper Award)</b> &nbsp;<a href="publication-conf_bib.html#wang2022local"+g' publication-conf.html

# add "Best Paper" to Zhixing's GECCO2023 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#huang2023grammar"+ <b style="color:red;">(GP Track Best Paper Award)</b> &nbsp;<a href="publication-conf_bib.html#huang2023grammar"+g' publication-conf.html

# add "Best Student Paper Runner-Up Award" to Trevor's AJCAI2023 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#londt2023xc"+ <b style="color:red;">(Best Student Paper Runner-Up Award)</b> &nbsp;<a href="publication-conf_bib.html#londt2023xc"+g' publication-conf.html