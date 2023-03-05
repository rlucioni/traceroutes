while true
do
    date -Iseconds >> google.txt
    traceroute -z 500 www.google.com >> google.txt

    date -Iseconds >> cloudflare.txt
    traceroute -z 500 1.1.1.1 >> cloudflare.txt

    sleep 60
done
