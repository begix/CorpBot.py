import asyncio
import discord
import sys
import traceback
from   discord.ext import commands
from   discord import errors
from   Cogs import Message

def setup(bot):
	bot.add_cog(Errors())

class Errors(commands.Cog):

	def __init__(self):
		pass

	@commands.Cog.listener()
	async def on_command_error(self, context, exception):
		if type(exception) is commands.CommandInvokeError:
			if type(exception.original) is discord.Forbidden:
				return await Message.EmbedText(
						title="⚠ Forbidden Error",
						color=context.author,
						description="(｡•́︿•̀｡)\nSepertinya aku mencoba melakukan sesuatu yang permissionnya tidak aku miliki!."
					).send(context)
			elif type(exception.original) is discord.errors.HTTPException and "Must be 2000 or fewer in length" in str(exception.original):
				return await Message.EmbedText(
						title="⚠ Terlalu banyak huruf",
						color=context.author,
						description="(｡•́︿•̀｡)\naku tidak dapat mengirim pesan lebih dari 2000 character!"
					).send(context)
		if str(exception).startswith("Music Cog: "):
			# Generic music exception - ignore
			return
		cog = context.cog
		if cog:
			attr = '_{0.__class__.__name__}__error'.format(cog)
			if hasattr(cog, attr):
				return
		print('Ignoring exception in command {}:'.format(context.command), file=sys.stderr)
		traceback.print_exception(type(exception), exception, exception.__traceback__, file=sys.stderr)

