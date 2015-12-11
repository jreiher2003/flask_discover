from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        # Ensure that login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue('Please login' in response.data)


        # ensure login behaves correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
	    	'/login', 
	    	data=dict(username='admin', 
	    		password='admin'),
	    	follow_redirects = True
    	)
    	self.assertTrue('You were logged in!', response.data)

        # incorrect creds
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
	    	'/login', 
	    	data=dict(username='wrong', 
	    		password='wrong'),
	    	follow_redirects = True
    	)
    	self.assertTrue('Invalid credentials. Please try again.', response.data)

        # logout
    def test_correct_logout(self):
        tester = app.test_client(self)
        response = tester.post(
	    	'/login', 
	    	data=dict(username='admin', 
	    		password='admin'),
	    	follow_redirects = True
    	)
    	response = tester.get('/logout', follow_redirects=True)
    	self.assertTrue('You were logged out!', response.data)

    	# ensure that the main page requires login
    def test_main_route_requires_login(self):
        tester = app.test_client()
        response = tester.get('/', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

     # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        tester = app.test_client()
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

    # Ensure that posts show up on the main page
    def test_posts_show_up_on_main_page(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'hello from the shell', response.data)

if __name__ == '__main__':
	unittest.main()