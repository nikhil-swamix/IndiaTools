import modulex as mx
import re
import os
import shutil
import glob

mx.require(['bs4', 'htmlmin', 'minify-html', 'lxml', 'css-html-js-minify'])

try:
    # from css_html_js_minify import html_minify, js_minify, css_minify
    import minify_html
except Exception:
    pass


def multiple_replace(dict, text):
    # Create a regular expression  from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)


def processor(fname):
    template = open(fname, 'r', encoding="utf-8").read()
    soupobj = mx.make_soup(template)

    for dtag in soupobj.select('[data-load]'):
        try:
            if (proxypath := dtag.get('data-load', None)):  # noqa: E225
                print("pp", proxypath)
                fileViewData = open(proxypath, encoding='utf-8').read()
                print(fileViewData)
                del dtag['data-load']
                dtag.append(mx.make_soup(fileViewData))

        except Exception as e:  # noqa: E722
        	print(e)

    minified = minify_html.minify(str(soupobj),
                                  do_not_minify_doctype=False,
                                  ensure_spec_compliant_unquoted_attribute_values=False,
                                  keep_closing_tags=True,
                                  keep_comments=False,
                                  keep_html_and_head_opening_tags=True,
                                  keep_spaces_between_attributes=False,
                                  minify_css=True,
                                  minify_js=True,
                                  remove_bangs=True,
                                  remove_processing_instructions=True)
    return minified


if __name__ == '__main__':
    os.chdir('../')
    os.makedirs('build', exist_ok=True)
    # os.chdir('build')

    for folder in ['assets', 'components']:
        shutil.copytree(folder, "build/" + folder, dirs_exist_ok=True)

    for file in glob.glob('*.html'):
    	mx.fwrite('build/'+file, processor(file))
    	# shutil.copy(file, 'build/'+file)

    # mx.fwrite('index.html', minified)
    print("==> DEV.HTML FILES HAVE BEEN MINIFIED")
