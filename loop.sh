while true
do
    date -Iseconds >> data/google.txt
    traceroute -q 1 -z 500 www.google.com >> data/google.txt

    date -Iseconds >> data/cloudflare.txt
    traceroute -q 1 -z 500 1.1.1.1 >> data/cloudflare.txt

    sleep 60
done
