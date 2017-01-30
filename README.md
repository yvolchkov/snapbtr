# snapbtr

snapbtr is a small utility that keeps snapshots of btrfs filesystems.

You can run it regularly (for example in a small script in
cron.hourly), or once in a while, to maintain an "interesting" (see
below) set of snapshots (backups). You may manually add or remove
snapshots as you like, use 'snapbtr.DATE_FORMAT' (in GMT) as
snapshot-name.

It will keep at most --target-backups snapshots and ensure that
--target-freespace is available on the file-system by selecting
snapshots to remove.

Using --keep-backups, you can ensure that at least some backups are
kept, even if --target-freespace cannot be satisfied.

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

I personally install snapbtr.py into /var/backups/snapbtr which is
only accessible to root and run it from a small script in
cron.hourly. I also install the kernel-nfs-server package and
nfs-export /var/backups/snapbtr in /etc/exports:

  /var/backups/snapbtr/     127.0.0.1(ro,no_root_squash,async,no_subtree_check)

and mount it at /mnt/restore, in /etc/fstab:

  localhost:/var/backups/snapbtr/ /mnt/restore nfs _netdev,nosuid,rsize=8192,hard,intr,ro  0 2

That way, all users can use the backups in /mnt/restore, but cannot
exploit security-bugs or tamper with the content.
