import openerp.tests

@openerp.tests.common.at_install(False)
@openerp.tests.common.post_install(True)
class TestUi(openerp.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "openerp.Tour.run('blog', 'test')", "openerp.Tour.tours.blog", login='admin')

