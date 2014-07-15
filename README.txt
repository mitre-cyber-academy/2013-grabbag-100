Name: Zipbomb
Description: Users will be provided with a docx file which the will not be able to open because the contents have been zip bombed and the headers of the word document have been corrupted. The users will be told that "Something happened to our newsletter template, can you help us fix it?" They will have to go in and either attempt to remove the zip bomb or simply dig through the images in the word document until they find the image containing the flag.
Notes: Users should only be provided with the newslettergenerated.docx file, the other one is the actual newsletter before it is zip bombed.
How to solve: The challenge can be solved by taking the document.xml file from this file and comparing it to one for a document that is still intact. When they do this they will notice the general metadata missing from the document and upon repair will be able to open the document and see the key.
Distribute: dist/newslettergenerated.docx
Flag: MCA-1E2C36AB