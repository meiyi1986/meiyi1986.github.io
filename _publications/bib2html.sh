 
bibtex2html/bibtex2html -nf pdf "PDF" -nf url_code "Code" -nf codec "C Code" -nf codecpp "C++ Code" -nf codemat "Matlab Code" -nf codejava "Java Code" -nf results Results publication-book.bib
bibtex2html/bibtex2html -nf pdf "PDF" -nf url_code "Code" -nf codec "C Code" -nf codecpp "C++ Code" -nf codemat "Matlab Code" -nf codejava "Java Code" -nf results Results publication-journal.bib
bibtex2html/bibtex2html -nf pdf "PDF" -nf url_code "Code" -nf codec "C Code" -nf codecpp "C++ Code" -nf codemat "Matlab Code" -nf codejava "Java Code" -nf results Results publication-conf.bib
bibtex2html/bibtex2html -nf pdf "PDF" -nf url_code "Code" -nf codec "C Code" -nf codecpp "C++ Code" -nf codemat "Matlab Code" -nf codejava "Java Code" -nf results Results publication-chapter.bib
chmod go+r *.html



# add "TEVC Outstanding Paper Award" to the DG paper
sed -i '' 's+\[&nbsp;<a href="publication-journal_bib.html#omidvar2014cooperative"+ <b style="color:red;">(TEVC Outstanding Paper Award)</b> &nbsp;<a href="publication-journal_bib.html#omidvar2014cooperative"+g' publication-journal.html

# add "Best Paper Runner-Up Award" to Fang's AI2018 MTGP paper
sed -i '' 's+pages 472--484. Springer, 2018.+pages 472--484. Springer, 2018. <b style="color:red;">(Best Paper Award Runner-Up)</b>+g' publication-conf.html

# add "Best Paper Runner-Up" to Alex's ICWS2018 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#da2018hybrid"+ <b style="color:red;">(Best Paper Award Runner-Up)</b> &nbsp;<a href="publication-conf_bib.html#da2018hybrid"+g' publication-conf.html

# add "Best Paper Nomination" to Alex's EvoCOP2016 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#da2016particle"+ <b style="color:red;">(Best Paper Nomination)</b> &nbsp;<a href="publication-conf_bib.html#da2016particle"+g' publication-conf.html

# add "Best Paper" to Zhixing's EuroGP2022 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#huang2022investigation"+ <b style="color:red;">(Best Paper Award)</b> &nbsp;<a href="publication-conf_bib.html#huang2022investigation"+g' publication-conf.html

# add "Best Paper" to Shaolin's GECCO2022 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#wang2022local"+ <b style="color:red;">(ECOM Track Best Paper Award)</b> &nbsp;<a href="publication-conf_bib.html#wang2022local"+g' publication-conf.html

# add "Best Paper" to Zhixing's GECCO2023 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#huang2023grammar"+ <b style="color:red;">(GP Track Best Paper Award)</b> &nbsp;<a href="publication-conf_bib.html#huang2023grammar"+g' publication-conf.html

# add "Best Student Paper Runner-Up Award" to Trevor's AJCAI2023 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#londt2023xc"+ <b style="color:red;">(Best Student Paper Award Runner-Up)</b> &nbsp;<a href="publication-conf_bib.html#londt2023xc"+g' publication-conf.html

# add "Beat Poster Runner-Up Award" to Nora's AJCAI2023 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#xu2023semantic"+ <b style="color:red;">(Best Poster Award Runner-Up)</b> &nbsp;<a href="publication-conf_bib.html#xu2023semantic"+g' publication-conf.html

# add "CIS Newsletter Research Frontier" to Nora's CIM2023 paper
sed -i '' 's+\[&nbsp;<a href="publication-journal_bib.html#xu2023genetic3"+ <b style="color:red;">(CIS Newsletter Research Frontier)</b> &nbsp;<a href="publication-journal_bib.html#xu2023genetic3"+g' publication-journal.html

# add "CIS Newsletter Research Frontier" to Yuzhou's CIM2023 paper
sed -i '' 's+\[&nbsp;<a href="publication-journal_bib.html#zhang2023rocash2"+ <b style="color:red;">(CIS Newsletter Research Frontier)</b> &nbsp;<a href="publication-journal_bib.html#zhang2023rocash2"+g' publication-journal.html

# add "Best Paper" to Xiaocheng's GECCO2024 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#liao2024learning"+ <b style="color:red;">(GP Track Best Paper Award)</b> &nbsp;<a href="publication-conf_bib.html#liao2024learning"+g' publication-conf.html

# add "Best Paper Nomination" to Jiyuan's GECCO2024 paper
sed -i '' 's+\[&nbsp;<a href="publication-conf_bib.html#pei2024learning"+ <b style="color:red;">(L4EC Track Best Paper Nomination)</b> &nbsp;<a href="publication-conf_bib.html#pei2024learning"+g' publication-conf.html
