from pages.base_page import Page


class Blog(Page):

    def verify_opened(self):
        self.verify_partial_url('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

