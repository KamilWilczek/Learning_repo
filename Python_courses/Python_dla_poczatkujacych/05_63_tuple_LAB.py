marketing = ['loyality program', 'client promotion', 'market reaserch']
print(marketing)

marketing.append('public relations')
print(marketing)

print(marketing[2])
marketing.insert(1,'investor relations')
print(marketing)
emailMarketing = marketing.copy()
print(emailMarketing)

emailMarketing.sort()
print(emailMarketing)

internalEmails = ['internal communication']
print(internalEmails)

emailMarketing.extend(internalEmails)
print(emailMarketing)
'''
9. Utwórz tuple, którego wartości pochodzą z listy emailMarketing.
Podczas wyświetlania tuple zwróć uwagę na nawiasy, z jakich skorzystał Python
'''
emailTuple = tuple(emailMarketing)
print(emailTuple)
