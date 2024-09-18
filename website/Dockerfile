# Use an official image for the web server (for example, NGINX)
FROM nginx:alpine

# Copy the website files from the repo to the web server's HTML directory
COPY ./website_files /usr/share/nginx/html

# Expose the default NGINX port
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
