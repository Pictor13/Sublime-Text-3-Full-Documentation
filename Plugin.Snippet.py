self.view.insert(edit, self.view.sel().end(), 'this char')   #insert text
self.view.run_command("toggle_setting", {"setting": "word_wrap"})
self.view.settings().set('syntax', 'Packages/Tidea/Tidea.tmLanguage')
sublime.set_clipboard('some message')
sublime.status_message('some message')
sublime.message_dialog('some message')
webbrowser.open_new_tab("file://" + self.view.file_name())	#Open in browser
ScopeName = self.view.scope_name(self.view.sel()[0].a)
ScopeText = self.view.substr(self.view.extract_scope(self.view.sel()[0].a))
fileName, fileExtension = os.path.splitext(self.view.file_name())
#Only run this plugin if
	def is_enabled(self):
		return self.view.file_name() != None and len(self.view.file_name()) > 0
#Delete a region of text
	SomeRegion.reverse()
    for r in SomeRegion:
       self.view.erase(edit, r)
sublime.set_timeout(lambda: self.view.window().run_command("find_next"), 100)   #wait 100ms then run "find_next" command
# Get selected text
	for region in self.view.sel():
		if not region.empty():
			s = self.view.substr(region)
			sublime.message_dialog(s)
sublime.message_dialog(self.view.substr(self.view.sel()[0]))