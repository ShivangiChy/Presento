import React from 'react';

const FooterInput = () => {
  return (
    <div className="mx-5 position:sticky relative bottom-0 flex flex-col justify-center min-h-screen ">
      <div >
        {/* <h1 className="text-3xl font-semibold text-center text-indigo-700 underline uppercase decoration-wavy">
          Contact Form
        </h1> */}
        <form className="mt-6">
          <div className="mb-2">
            <label>
              {/* <span className="text-gray-700">Your name</span> */}
              <input
                type="link"
                name="link"
                className="

            w-full
            block px-16 py-2 mt-2
            border-gray-300
            rounded-md
            shadow-sm
            focus:border-indigo-300
            focus:ring
            focus:ring-indigo-200
            focus:ring-opacity-50
          "
                placeholder="Enter article link"
              />
            </label>
          </div>
          {/* <div className="mb-2">
            <label>
              <span className="text-gray-700">Email address</span>
              <input
                name="email"
                type="email"
                className="
            block
            w-full
            mt-2 px-16 py-2
            border-gray-300
            rounded-md
            shadow-sm
            focus:border-indigo-300
            focus:ring
            focus:ring-indigo-200
            focus:ring-opacity-50
          "
                placeholder="john.cooks@example.com"
                required
              />
            </label>
          </div> */}
          <div className="mb-2">
            <label>
              {/* <span class="text-gray-700">Message</span> */}
              <textarea
                name="message"
                className="
            block
            w-full
            mt-2 px-16 py-8
            border-gray-300
            rounded-md
            shadow-sm
            focus:border-indigo-300
            focus:ring
            focus:ring-indigo-200
            focus:ring-opacity-50
          "
          placeholder="Enter article text"
                rows="5"
              ></textarea>
            </label>
          </div>

          <div class="mb-6">
            <button
              type="submit"
              className="
            h-10
            px-5
            text-indigo-100
            bg-gray-800
            rounded-lg
            transition-colors
            duration-150
            focus:shadow-outline
            hover:bg-indigo-800
          "
            >
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default FooterInput;