# Gebruik Ubuntu als basis
FROM ubuntu:22.04

# Update en installeer Lighttpd
RUN apt-get update && \
    apt-get install -y lighttpd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Kopieer je HTML-bestand
COPY index.html /var/www/html/index.html

# Expose poort 80
EXPOSE 80

# Start Lighttpd in foreground
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
