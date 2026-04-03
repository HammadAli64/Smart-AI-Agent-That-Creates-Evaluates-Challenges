/** @type {import('next').NextConfig} */
const nextConfig = {
  output: "standalone",
  reactStrictMode: true,
  devIndicators: {
    buildActivity: false
  },
  async redirects() {
    return [
      { source: "/challenges", destination: "/", permanent: false },
      { source: "/challenges/:path*", destination: "/", permanent: false }
    ];
  }
};

module.exports = nextConfig;

