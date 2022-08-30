import keyboard
import multiprocessing
import time
import yiceda
import schedule

def run():
  print('start report ...')
  yiceda.report_health_info()

schedule.every().day.at("06:20").do(run)

def schedule_run():
  while True:
    schedule.run_pending()
    time.sleep(300)

if __name__=='__main__':
  print('welcome!') 
  p1 = multiprocessing.Process(target=schedule_run,args=())
  p1.start() 
  print('press space to exit!') 
  keyboard.wait('space')
  p1.terminate()
