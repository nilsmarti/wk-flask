# WaniKani Dashboard implemented in Flask

Simple Flask app to retrieve data from the WaniKani API. Currently the app retrieves the user's level, lessons and reviews pending. If you want to add more fields, feel free to open an issue or pull request.

## Self-Hosting

To self-host the app, you can use Docker. Here's a quick guide:

1. Install Docker on your system.
2. Pull the image from this repository:

   ```bash
   docker pull ghcr.io/nilsmarti/wk-flask:latest
   ```

3. Run the image:

   ```bash
   docker run -d -p 5000:5000 ghcr.io/nilsmarti/wk-flask:latest
   ```

4. Open your web browser and navigate to `http://localhost:5000`.

### To use a unstable version:

1. Pull the image from this repository:

   ```bash
   docker pull ghcr.io/nilsmarti/wk-flask:dev
   ```

2. Run the image:

   ```bash
   docker run -d -p 5000:5000 ghcr.io/nilsmarti/wk-flask:dev
   ```

3. Open your web browser and navigate to `http://localhost:5000`.


## Contributing

Please feel free to open an issue or pull request if you have any suggestions or improvements. This is a hobby project, so don't expect your issues to be resolved quickly. Feel free to submit a pull request with your changes, and I'll review them as soon as possible.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
