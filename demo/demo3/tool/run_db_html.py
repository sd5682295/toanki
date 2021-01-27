from run_html import run_html

class run_db_html(run_html):
    pass
if __name__ == "__main__":
    rh = run_db_html(ihtml='../html/测试方法和流程拆分出的内容.html', out_path='../anki_txt/')
    rh.run()