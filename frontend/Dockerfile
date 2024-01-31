FROM nginx:alpine

# Copy the content of the local frontend directory to the container
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# CMD instruction to start Nginx
CMD ["nginx", "-g", "daemon off;"]
