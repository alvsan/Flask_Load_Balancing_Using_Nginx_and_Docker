from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    #return f"Hello, this is an application running on {socket.gethostname()}"
    #return f"<p style='text-align: center; color:#{socket.gethostname()[:6]}; background-color:#{socket.gethostname()[6:]}'>Hello, this is an application running on container-id: {socket.gethostname()}.</p>"
    return f"<p style='text-align: center; color:{invertColor(socket.gethostname()[6:], bw=True)}; background-color:#{socket.gethostname()[6:]}'>Hello, this is an application running on container-id: {socket.gethostname()}.</p>"

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def invertColor(color, bw=False):
    # strip the # from the beginning
    color = color.lstrip('#')

    # convert the string into hex
    color = int(color, 16)

    # invert the three bytes
    # as good as substracting each of RGB component by 255(FF)
    comp_color = 0xFFFFFF ^ color

    # convert the color back to hex by prefixing a #
    comp_color = "#%06X" % comp_color

    rgb_color = hex_to_rgb(comp_color)

    if (bw):
        # http://stackoverflow.com/a/3943023/112731
        bw_value = rgb_color[0]*0.299 + rgb_color[0]*0.587 + rgb_color[0]*0.114
        if (bw_value>186):
            comp_color = "#FFFFFF"
        else:
            comp_color = "#000000"

    # return the result
    return comp_color

if __name__ == "__main__":
    app.run(debug=True)
