#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainPage(webapp2.RequestHandler):
    def write_form(error=""):
        self.response.out.write(form%{"error":error})
    
    def get(self):
        self.write.form()
    
    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))
        
        if not (user_month and user_day and user_year):
            self.write.form("That doesn't look valid to me, friend.")
        else:
            self.response.out.write("Thanks That's a totally valid day!")

app = webapp2.WSGIApplication([
                               ('/', MainPage),
                               ], debug=True)
