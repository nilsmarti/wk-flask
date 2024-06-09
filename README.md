# WaniKani Dashboard implemented in Flask

Simple Flask app to retrieve data from the WaniKani API.

## Self-Hosting

To self-host the app, you can use Docker. Here's a quick guide:

1. Install Docker on your system.
2. Pull the image from this repository:

   ```bash
   docker pull ghcr.io/nilsmarti/wk-flask:main
   ```

3. Run the image:

   ```bash
   docker run -d -p 5000:5000 ghcr.io/nilsmarti/wk-flask:main
   ```

4. Open your web browser and navigate to `http://localhost:5000`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
