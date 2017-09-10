# snapbtr

snapbtr is a small utility that keeps snapshots of btrfs filesystems.

It is originally written by Helge Jensen
(https://btrfs.wiki.kernel.org/index.php/SnapBtr). Re-published under
the GPLv3 with his consent and blessing.

You can run it regularly (for example in a small script in
cron.hourly), or once in a while, to maintain an "interesting" (see
below) set of snapshots (backups). You may manually add or remove
snapshots as you like, use 'snapbtr.DATE_FORMAT' (in GMT) as
snapshot-name.

It will keep --target-backups snapshots on the file-system by
selecting snapshots to remove.

Using --preserve-days, you can ensure that the most recent snapshots,
which are taken within last N days are not deleted.

snapnbtr will keep backups with exponentially increasing distance as
you go back in time. It does this by selecting snapshots to remove as
follows.

The snapshots to remove is selected by "scoring" each space between
snapshots, (newer,older). snapbtr will remove the older of the two
snapshots in the space that have the lowest score.

The scoring mechanism integrates e^x from (now-newer) to (now-older)
so, new pairs will have high value, even if they are tightly packed,
while older pairs will have high value if they are far apart.

The mechanism is completely self-contained and you can delete any
snapshot manually or any files in the snapshots.

Root permissions are not required for _creating_ snapshot, if user has
an ownership of the subvolume. This makes it possible to run "snapbtr
-s" from a user application prior any modification done by this
application (e.g. snapshot a maildir before receiving new emails). And
periodically run "snapbtr -c" as root to cleanup.

# Examples
Snapshot maildir before synchronization
```
snapbtr -s ~/email/store ~/email/backups
```

From all the backups which older then 5 days, keep only 100.
```
./snapbtr -c /mnt/backups  --target-backups 100 --preserve-days 5
```

Do the same, but create the snapshot at first
```
./snapbtr -cs ~/email/store ~/email/backups  --target-backups 100 --preserve-days 5
```

# Install

```
sudo python2 setup.py install
```

or

```
sudo pip install snapbtr
```

# Authors

* Helge Jensen <hej@actua.dk>
* Yuri Volchkov <yuri.volchkov@gmail.com>

Licensed under GPLv3 (or later) <http://www.gnu.org/licenses/gpl-3.0.txt>
