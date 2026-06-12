import os

from database import (
    add_homework,
    get_homework
)

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "Hello Nihal! JEE Study OS is running."
    )


async def addhw(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if len(context.args) < 2:

        await update.message.reply_text(
            "Usage:\n/addhw SUBJECT TASK"
        )

        return

    subject = context.args[0]

    task = " ".join(
        context.args[1:]
    )

    add_homework(
        subject,
        task
    )

    await update.message.reply_text(
        f"✅ Added:\n{subject} - {task}"
    )


async def tasks(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = get_homework()

    if len(data) == 0:

        await update.message.reply_text(
            "No homework."
        )

        return

    text = "📚 Homework\n\n"

    for row in data:

        text += (
            f"• {row[0]} - {row[1]}\n"
        )

    await update.message.reply_text(
        text
    )


def main():

    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        CommandHandler(
            "addhw",
            addhw
        )
    )

    app.add_handler(
        CommandHandler(
            "tasks",
            tasks
        )
    )

    app.run_polling()


if __name__ == "__main__":
    main()import os

from database import (
    add_homework,
    get_homework
)

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "Hello Nihal! JEE Study OS is running."
    )

async def addhw(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if len(context.args) < 2:

        await update.message.reply_text(
            "Usage:\n/addhw SUBJECT TASK"
        )

        return

    subject = context.args[0]

    task = " ".join(
        context.args[1:]
    )

    add_homework(
        subject,
        task
    )

    await update.message.reply_text(
        f"✅ Added:\n{subject} - {task}"
    )
    
    async def tasks(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = get_homework()

    if len(data) == 0:

        await update.message.reply_text(
            "No homework."
        )

        return

    text = "📚 Homework\n\n"

    for row in data:

        text += (
            f"• {row[0]} - "
            f"{row[1]}\n"
        )

    await update.message.reply_text(
        text
    )
    
def main():

    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )
    app.add_handler(
        CommandHandler(
            "addhw",
            addhw
        )
    )

    app.add_handler(
        CommandHandler(
            "tasks",
            tasks
        )
    )
    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.run_polling()

if __name__ == "__main__":
    main()