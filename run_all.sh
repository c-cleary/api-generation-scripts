if [ ! -d "./logs" ]
then
    mkdir logs
fi
sh doc_command_all.sh 2> logs/all.log
echo "Xdoclint:all finished 1/6"
sh doc_command_accessibility.sh 2> logs/accessibility.log
echo "Xdoclint:accessibility finished 2/6"
sh doc_command_missing.sh 2> logs/missing.log
echo "Xdoclint:missing finished 3/6"
sh doc_command_html.sh 2> logs/html.log
echo "Xdoclint:html finished 4/6"
sh doc_command_reference.sh 2> logs/reference.log
echo "Xdoclint:reference finished 5/6"
sh doc_command_syntax.sh 2> logs/syntax.log
echo "Xdoclint:syntax finished 6/6"
echo "All runs complete."
