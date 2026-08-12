const verificationRoutes = {"/google939576fea7c9232c.html": {"content": "google-site-verification: google939576fea7c9232c.html\n", "contentType": "text/html; charset=UTF-8"}, "/BingSiteAuth.xml": {"content": "<?xml version=\"1.0\"?>\n<users>\n  <user>DC4AB582C527A7A168FC391B84B8995E</user>\n</users>\n", "contentType": "application/xml; charset=UTF-8"}};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const verification = verificationRoutes[url.pathname];
    if (verification) {
      return new Response(verification.content, {
        status: 200,
        headers: {
          "content-type": verification.contentType,
          "cache-control": "no-store"
        }
      });
    }
    return env.ASSETS.fetch(request);
  }
};
