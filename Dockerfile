# Use the official Nginx image
FROM nginx:alpine

# Copy our index.html to the default Nginx location
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]


