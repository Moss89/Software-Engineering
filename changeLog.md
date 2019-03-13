

************************************************
Date:              13/02/2019        
Author:            Tomas

Changes: Change log file created.
************************************************

commit 719de4a (HEAD -> MidtermRefactor, origin/MidtermRefactor)
Author: jmcl <john.mc-loughlin.3@ucdconnect.ie>
Date:   Sat Mar 9 14:13:30 2019 +0000

    Ajax implemented
    Query SQL to get address and number of available bikes for a specific time and date
    Still need to get these numbers to print on the bike markers
    
    Signed-off-by: jmcl <john.mc-loughlin.3@ucdconnect.ie>

commit 11d01f1
Author: jmcl <john.mc-loughlin.3@ucdconnect.ie>
Date:   Sat Mar 9 14:04:47 2019 +0000

    Ajax implemented
    Query SQL to get address and number of available bikes for a specific time and date
    Still need to get these numbers to print on the bike markers
    
    Signed-off-by: jmcl <john.mc-loughlin.3@ucdconnect.ie>

commit d26805f
Author: jmcl <john.mc-loughlin.3@ucdconnect.ie>
Date:   Fri Mar 8 18:09:35 2019 +0000

    Most stuff integrated
    Still need to get calendar css working and jquery stuff
    Started commenting but don't have time today to go through html
    Still need to implement Ajax
    
    Signed-off-by: jmcl <john.mc-loughlin.3@ucdconnect.ie>

commit 66fc2bc
Author: jmcl <john.mc-loughlin.3@ucdconnect.ie>
Date:   Fri Mar 8 17:52:46 2019 +0000

    Most stuff integrated
    Still need to get calendar css working and jquery stuff
    Started commenting but don't have time today to go through html
    Still need to implement Ajax
    
    Signed-off-by: jmcl <john.mc-loughlin.3@ucdconnect.ie>

commit f71a703 (origin/Staging, Staging)
Author: Tom <Tomas.Murphy2@gmail.com>
Date:   Thu Mar 7 10:08:50 2019 +0000

    Fixed website JS issues.
    
    Signed-off-by: Tom <Tomas.Murphy2@gmail.com>

commit e1fe6d1
Author: Tom <Tomas.Murphy2@gmail.com>
Date:   Thu Mar 7 09:29:03 2019 +0000

    Added images to website.
    
    Signed-off-by: Tom <Tomas.Murphy2@gmail.com>

commit b7ba6a5
Author: Tom <Tomas.Murphy2@gmail.com>
Date:   Thu Mar 7 09:01:57 2019 +0000

    Added weather widget to website.
    
    Signed-off-by: Tom <Tomas.Murphy2@gmail.com>

commit 6097e87
Author: Tom <Tomas.Murphy2@gmail.com>
Date:   Tue Mar 5 09:20:52 2019 +0000

    Added website & updated image links
    
    Signed-off-by: Tom <Tomas.Murphy2@gmail.com>

commit d094881
Author: Tom <Tomas.Murphy2@gmail.com>
Date:   Mon Mar 4 17:08:23 2019 +0000

    Timer now actually updating properly
    
    Signed-off-by: Tom <Tomas.Murphy2@gmail.com>

commit a32d301
Merge: 0341b79 0c233ea
Author: Tom <Tomas.Murphy2@gmail.com>
Date:   Mon Mar 4 17:07:14 2019 +0000

    Merge branch 'Staging' of https://github.com/Moss89/DublinBikesProject into Staging

commit 0341b79
Author: Tom <Tomas.Murphy2@gmail.com>
Date:   Mon Mar 4 17:05:17 2019 +0000

    Timer now actually updating properly
    
    Signed-off-by: Tom <Tomas.Murphy2@gmail.com>

commit 0c233ea
Merge: 8872b80 cf487aa
Author: john <john.hackett1@ucdconnect.ie>
Date:   Wed Feb 27 11:29:30 2019 +0000

    Adding the flask app and html file to display map markers by probing with google maps js api

commit cf487aa
Author: john <john.hackett1@ucdconnect.ie>
Date:   Wed Feb 27 11:28:03 2019 +0000

    Added the flask script and html file for google maps

commit 8872b80
Merge: 50ba1aa 19894e9
Author: john <john.hackett1@ucdconnect.ie>
Date:   Tue Feb 26 19:37:05 2019 +0000

    Merge remote-tracking branch 'Dublin_Bikes/FlaskSQL' into Staging

commit 19894e9
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Tue Feb 26 19:08:54 2019 +0000

    flask_sqlalchemy connecting to local database
    Can use python shell to execute sql commands
    Need to be able to post results on webpage next
    
    Signed-off-by: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>

commit 50ba1aa
Author: Tom <Tomas.Murphy2@gmail.com>
Date:   Tue Feb 26 10:18:35 2019 +0000

    Weather Scraper Added TM 26/02/19
    
    Signed-off-by: Tom <Tomas.Murphy2@gmail.com>

commit 6b76dea
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Tue Feb 26 10:11:05 2019 +0000

    changes

commit 5fde3ff
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Tue Feb 26 10:09:56 2019 +0000

    removed weatherscraper

commit f4a8dc7
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Sat Feb 23 22:27:55 2019 +0000

    Timer now actually updating properly
    
    Signed-off-by: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>

commit 48258c9
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Sat Feb 23 21:29:29 2019 +0000

    Moved time outside for loop in create_sql_query
    
    Signed-off-by: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>

commit d7f0009
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Sat Feb 23 20:57:29 2019 +0000

    Just changing the database name

commit 41eafc2
Merge: 967fc24 ef88614
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Sat Feb 23 20:48:32 2019 +0000

    Merge branch 'Staging'

Testing that merge works
Also new scraper code with the database url in it

commit ef88614
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Sat Feb 23 18:10:22 2019 +0000

    Also updated SQL address
    
    Signed-off-by: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>

commit b90c024
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Sat Feb 23 18:07:50 2019 +0000

    Not backing up to CSV in case we use up free storage on EC2
    
    Signed-off-by: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>

commit 967fc24
Author: Moss89 <35338105+Moss89@users.noreply.github.com>
Date:   Fri Feb 22 12:40:34 2019 +0000

    Add files via upload

commit d84485b
Author: Tom <Tomas.Murphy2@gmail.com>
Date:   Fri Feb 22 12:30:29 2019 +0000

    Bike and weather scraper

commit 83c2cf9
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Fri Feb 22 12:08:20 2019 +0000

    Scraper timestamp taken from computer rather than API so it'll actually change with every sQL write
    Broke out main write function into smaller functions for readability and maintainability
    
    Signed-off-by: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>

commit 26d018e
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Tue Feb 19 19:30:15 2019 +0000

    Added shebang to DBScraper.py so it'll run in background
    Instructions for running commented above shebang
    
    Signed-off-by: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>

commit b87b756
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Tue Feb 19 17:57:12 2019 +0000

    Moved total number of bikestands from dynamic info to static info
    Cleared out backup csvs so that they're not full of data from tests
    
    Signed-off-by: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>

commit 24bb472
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Tue Feb 19 14:36:23 2019 +0000

    DBSCreateStaticTables.py now creates DbDynamicInfo as well as DbStaticInfo
    DBSCreateStaticTables.py renamed to DBSCreateTables.py
    
    Signed-off-by: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>

commit 16c75f2
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Mon Feb 18 20:42:58 2019 +0000

    Now with comments
    Also csv files are now empty
    
    Signed-off-by: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>

commit 2dd2ca2
Author: John McLoughlin <john.mc-loughlin.3@ucdconnect.ie>
Date:   Mon Feb 18 20:32:00 2019 +0000

    DBScraper.py stores dynamic data from dublin bikes api, runs continuously
    DBSCreateStaticTable stores static data from dublin bikes api, runs once
    Backups for both created with dynamic updated as sql updates
    Need to setup backup to google team drives for csvs

commit 87ebf45
Author: Moss89 <35338105+Moss89@users.noreply.github.com>
Date:   Wed Feb 13 12:46:55 2019 +0000

    Update changeLog.md

commit 7c9e4d9
Author: Moss89 <35338105+Moss89@users.noreply.github.com>
Date:   Wed Feb 13 12:46:40 2019 +0000

    Update changeLog.md

commit 40164ab
Author: jmcl001 <43282116+jmcl001@users.noreply.github.com>
Date:   Wed Feb 13 12:45:41 2019 +0000

    Delete CHANGELOG.md

commit e251d7d
Author: Moss89 <35338105+Moss89@users.noreply.github.com>
Date:   Wed Feb 13 12:45:29 2019 +0000

    Rename changeLog.txt to changeLog.md

commit fa56ca8
Author: Moss89 <35338105+Moss89@users.noreply.github.com>
Date:   Wed Feb 13 12:44:23 2019 +0000

    Create changeLog.txt

commit 40c2e6b
Author: jmcl001 <43282116+jmcl001@users.noreply.github.com>
Date:   Wed Feb 13 12:40:53 2019 +0000

    Create CHANGELOG.md

commit dcee870
Author: Moss89 <35338105+Moss89@users.noreply.github.com>
Date:   Wed Feb 13 12:36:15 2019 +0000

    Initial commit
