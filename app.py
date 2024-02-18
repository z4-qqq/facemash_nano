from flask import Flask, render_template, request, redirect, url_for
from utils.create import create_tournament
from data.local import collect_images
from data.parse_args import get_argparser
app = Flask(__name__)


@app.route('/')
def index():
    """Render two images for tournament."""
    # Render the template with the first two images
    tournament_round = tournament.get_round()
    if tournament_round is not None:
        image1, image2 = tournament_round
    else:
        raise ValueError("Tournament pairs are ended. Something went wrong")
    return render_template('index.html', image1=image1, image2=image2)


@app.route('/vote', methods=['POST'])
def vote():
    """Voting for best image.
    If this is the last round the winner will be shown.
    """
    selected_image = request.form['selected_image']
    # Save the winner
    tournament.update_winners(winner=selected_image)

    # If there are more images, redirect to the voting page with the next two images
    if len(tournament.pairs) > 0:
        return redirect(url_for('index'))
        # Check for winners:
    if len(tournament.winners) == 1:
        return redirect(url_for('result'))
    else:
        tournament.update_pairs()
        return redirect(url_for('index'))


@app.route('/result')
def result():
    """Render winner image"""
    return render_template("result.html", winner=tournament.winners[0])


if __name__ == '__main__':
    args = get_argparser().parse_args()
    images = collect_images(data_format=args.data_format)
    tournament = create_tournament(images=images)
    app.run(debug=True)
