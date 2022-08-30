import keyboard
import multiprocessing
import time
import yiceda
import schedule
# from apscheduler.schedulers.blocking import BlockingScheduler

def run():
  print('start report ...')
  #归位
  yiceda.report_health_info()

schedule.every().day.at("15:07").do(run)
schedule.every().minute.at(':30').do(run)
schedule.every().minute.at(':01').do(run)

def schedule_run():
  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__=='__main__':
  print('welcome!') 
  # sched = BlockingScheduler()
  # sched.add_job(run, 'cron', day_of_week='mon-fri', hour=6, minute=30, end_date='2022-08-31')
  # sched.start()
  p1 = multiprocessing.Process(target=schedule_run,args=())
  p1.start() 
  print('press space to exit!') 
  keyboard.wait('space')
  p1.terminate()