"""This file is executed on every boot (including wake-boot from deepsleep). It allows us to write data to a file"""
import storage
storage.remount("/", readonly=False)